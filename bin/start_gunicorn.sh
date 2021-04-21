source /home/alex/code/content_bloks/env/bin/activate
exec gunicorn -c "/home/alex/code/content_bloks/content_blocks/gunicorn_config.py" content_blocks.wsgi
