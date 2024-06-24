echo start de testrun

#onderstaande uitzetten voor headless
pytest --headed --slowmo 100 -o cache_dir=/cache

#onderstaande aanzetten voor headless
#pytest -o cache_dir=/cache 