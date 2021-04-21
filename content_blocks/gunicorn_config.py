command = '/home/alex/code/content_bloks/env/bin/gunicorn'
pythonpath = '/home/alex/code/content_bloks/content_blocks'
bind = '127.0.0.1:8035'
workers = 3
user = 'alex'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=content_blocks.settings'
