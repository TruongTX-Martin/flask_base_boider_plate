build:
	@docker-compose build

local:
	@docker-compose down && docker-compose -f docker-compose.yml up -d --remove-orphans

development:
	@docker-compose down && docker-compose -f docker-compose.yml -f docker-compose.development.yml up -d --remove-orphans

build-production:
	@docker-compose -f docker-compose.production.yml build

production:
	@docker-compose -f docker-compose.production.yml down -v && docker-compose -f docker-compose.production.yml up -d --remove-orphans
