run-dev:
	docker build -t dc-docker .
	docker run -d -p 80:80 -v %cd%:/app dc-docker /start-reload.sh