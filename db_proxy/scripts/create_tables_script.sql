USE shortpy_stage_db;

CREATE TABLE IF NOT EXISTS `users` (
  `id` BIGINT UNSIGNED PRIMARY KEY NOT NULL,
  `email` varchar(255) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `urls` (
  `id` BIGINT UNSIGNED PRIMARY KEY NOT NULL,
  `original_url` varchar(2500) NOT NULL,
  `short_url` varchar(50) NOT NULL,
  `user_id` BIGINT UNSIGNED NOT NULL,
  `created_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `expires_at` TIMESTAMP DEFAULT NULL
);

CREATE TABLE IF NOT EXISTS `clicks` (
  `id` BIGINT UNSIGNED PRIMARY KEY NOT NULL,
  `url_id` BIGINT UNSIGNED NOT NULL,
  `clicked_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  `ip_address` varchar(255),
  `user_agent` varchar(255)
);

ALTER TABLE `urls` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `clicks` ADD FOREIGN KEY (`url_id`) REFERENCES `urls` (`id`);
