echo start de testrun

#onderstaande uitzetten voor headless
pytest --headed -o cache_dir=/cache

#onderstaande aanzetten voor headless
#pytest -o cache_dir=/cache 