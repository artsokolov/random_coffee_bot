build:
	docker-compose build

run:
	docker-compose up -d

down:
	docker-compose down --remove-orphans

restart:
	docker-compose restart app

app-logs:
	docker-compose logs -f app