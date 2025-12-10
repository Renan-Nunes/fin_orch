from logging.config import fileConfig
import sys
import os

# Adiciona o diretório raiz do projeto ao path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sqlalchemy import engine_from_config, pool
from alembic import context
from app.config.config import url_db
from app.models.base_config import Base
import app.models

# Config Alembic
config = context.config
config.set_main_option("sqlalchemy.url", url_db)
fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
