import os
import logging
import connexion
from logging.handlers import RotatingFileHandler
from peewee_migrate.router import Router, load_models
from peewee_migrate.auto import diff_many
import pavlov_central.storage
from pavlov_central.storage.models.base_model import DB
from pavlov_central.api.encoder import JSONEncoder


def start_api():
    app = connexion.FlaskApp(__name__, specification_dir='./api/openapi/')
    app.app.json_encoder = JSONEncoder
    app.app.config['JSON_SORT_KEYS'] = False
    app.add_api('openapi.yaml')
    app.run(port=5000)


def init_logging():
    r_handler = RotatingFileHandler(
        filename='/tmp/pavlov_central.log', maxBytes=1000000, backupCount=3
    )
    r_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(threadName)s %(funcName)s: %(message)s"))
    logging.getLogger().addHandler(r_handler)
    logging.getLogger().setLevel(logging.DEBUG)


def run_db_migration(database):
    db_storage_dir = os.path.dirname(pavlov_central.storage.__file__)
    print(f'db_storage_dir={db_storage_dir}')
    db_migrations_dir = os.path.join(db_storage_dir, 'migrations')
    print(f'db_migrations_dir={db_migrations_dir}')

    router = Router(
        database,
        migrate_dir=db_migrations_dir,
        migrate_table='migration',
        logger=logging.getLogger(),
        ignore=['basemodel', 'basedatamodel', 'frs5model', 'virtualmodel', 'baseftsmodel', 'ftsmodel', 'lsmtable']
    )
    print('Run migrations..')

    router.run()

    # check migrations
    src_models = load_models('pavlov_central.storage.models')
    print(f'src_models={src_models}')
    if router.ignore:
        src_models = [m for m in src_models if m.get_table_name() not in router.ignore]

    db_models = router.migrator.orm.values()
    print(f'db_models={db_models}')

    diff_found = diff_many(src_models, db_models, router.migrator, reverse=False)

    if len(diff_found) > 0:
        logging.warning('migrations diff_found={}'.format(diff_found))
        print('migrations diff_found={}'.format(diff_found))
        raise RuntimeError('Check db migrations is failed')


if __name__ == '__main__':
    init_logging()
    run_db_migration(DB)
    start_api()
