import logging
from typing import Generic, TypeVar

from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import func
from sqlalchemy import update as sqlalchemy_update
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy.future import select

from uv_project_ty_ruff_bitbucket_streamlit.db.sync.engine import Base
from uv_project_ty_ruff_bitbucket_streamlit.schemas import BaseORMFilterModel, BaseORMModel

T = TypeVar("T", bound=Base)
F = TypeVar("F", bound=BaseORMFilterModel)
V = TypeVar("V", bound=BaseORMModel)


logger = logging.getLogger("dao.base")


class BaseDAO(Generic[T]):
    model: type[T] = None

    def __init__(self, session: Session):
        self._session = session
        if self.model is None:
            raise ValueError("Model must be specified in the child class")

    def find_one_or_none_by_id(self, data_id: int) -> type[T]:
        try:
            query = select(self.model).filter_by(id=data_id)
            result = self._session.execute(query)
            record = result.scalar_one_or_none()
            log_message = f"Record {self.model.__name__} with ID {data_id} {'found' if record else 'not found'}."
            logger.info(log_message)
            return record
        except SQLAlchemyError as e:
            logger.error(f"Error while searching for record with ID {data_id}: {e}")
            raise

    def find_one_or_none(self, filters: type[F]) -> type[T]:
        # NOTE: `exclude_unset` - excludes even default values, only explicit __init__ args are kept
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Searching for one record {self.model.__name__} by filters: {filter_dict}")
        try:
            query = select(self.model).filter_by(**filter_dict)
            result = self._session.execute(query)
            record = result.scalar_one_or_none()
            log_message = f"Record {'found' if record else 'not found'} by filters: {filter_dict}"
            logger.info(log_message)
            return record
        except SQLAlchemyError as e:
            logger.error(f"Error while searching for record by filters {filter_dict}: {e}")
            raise

    def find_all(self, filters: type[F] | None = None) -> list[type[T]]:
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f"Searching for all records {self.model.__name__} by filters: {filter_dict}")
        try:
            query = select(self.model).filter_by(**filter_dict)
            result = self._session.execute(query)
            records = result.scalars().all()
            logger.info(f"Found {len(records)} records.")
            return records
        except SQLAlchemyError as e:
            logger.error(f"Error while searching for all records by filters {filter_dict}: {e}")
            raise

    def add(self, values: type[V]) -> type[T]:
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Adding record {self.model.__name__} with parameters: {values_dict}")
        try:
            new_instance = self.model(**values_dict)
            self._session.add(new_instance)
            logger.info(f"Record {self.model.__name__} successfully added.")
            self._session.flush()
            return new_instance
        except SQLAlchemyError as e:
            logger.error(f"Error while adding record: {e}")
            raise

    def add_or_update(self, values: type[V]) -> type[T]:
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(f"Adding record {self.model.__name__} with parameters: {values_dict}")
        try:
            new_instance = self.model(**values_dict)
            self._session.add(new_instance)
            logger.info(f"Record {self.model.__name__} successfully added.")
            self._session.flush()
            return new_instance
        except SQLAlchemyError as e:
            logger.error(f"Error while adding record: {e}")
            raise

    def add_many(self, instances: list[type[V]]) -> list[type[T]]:
        values_list = [item.model_dump(exclude_unset=True) for item in instances]
        logger.info(f"Adding multiple records {self.model.__name__}. Count: {len(values_list)}")
        try:
            new_instances = [self.model(**values) for values in values_list]
            self._session.add_all(new_instances)
            logger.info(f"Successfully added {len(new_instances)} records.")
            self._session.flush()
            return new_instances
        except SQLAlchemyError as e:
            logger.error(f"Error while adding multiple records: {e}")
            raise

    def update(self, filters: type[F], values: type[V]) -> int:
        filter_dict = filters.model_dump(exclude_unset=True)
        values_dict = values.model_dump(exclude_unset=True)
        logger.info(
            f"Updating records {self.model.__name__} by filter: {filter_dict} with parameters: {values_dict}"
        )
        try:
            query = (
                sqlalchemy_update(self.model)
                .where(*[getattr(self.model, k) == v for k, v in filter_dict.items()])
                .values(**values_dict)
                .execution_options(synchronize_session="fetch")
            )
            result = self._session.execute(query)
            logger.info(f"Updated {result.rowcount} records.")
            self._session.flush()
            return result.rowcount
        except SQLAlchemyError as e:
            logger.error(f"Error while updating records: {e}")
            raise

    def delete(self, filters: type[F]):
        filter_dict = filters.model_dump(exclude_unset=True)
        logger.info(f"Deleting records {self.model.__name__} by filter: {filter_dict}")
        if not filter_dict:
            logger.error("At least one filter is required for deletion.")
            raise ValueError("At least one filter is required for deletion.")
        try:
            query = sqlalchemy_delete(self.model).filter_by(**filter_dict)
            result = self._session.execute(query)
            logger.info(f"Deleted {result.rowcount} records.")
            self._session.flush()
            return result.rowcount
        except SQLAlchemyError as e:
            logger.error(f"Error while deleting records: {e}")
            raise

    def count(self, filters: type[F] | None = None) -> int:
        filter_dict = filters.model_dump(exclude_unset=True) if filters else {}
        logger.info(f"Counting records {self.model.__name__} by filter: {filter_dict}")
        try:
            query = select(func.count(self.model.id)).filter_by(**filter_dict)
            result = self._session.execute(query)
            count = result.scalar()
            logger.info(f"Found {count} records.")
            return count
        except SQLAlchemyError as e:
            logger.error(f"Error while counting records: {e}")
            raise

    def bulk_update(self, records: list[type[V]]) -> list[type[T]]:
        logger.info(f"Mass update of records {self.model.__name__}")
        try:
            updated_count = 0
            for record in records:
                record_dict = record.model_dump(exclude_unset=True)
                if "id" not in record_dict:
                    continue

                update_data = {k: v for k, v in record_dict.items() if k != "id"}
                stmt = (
                    sqlalchemy_update(self.model)
                    .filter_by(id=record_dict["id"])
                    .values(**update_data)
                )
                result = self._session.execute(stmt)
                updated_count += result.rowcount

            logger.info(f"Updated {updated_count} records")
            self._session.flush()
            return updated_count
        except SQLAlchemyError as e:
            logger.error(f"Error while mass updating: {e}")
            raise
