CREATE TABLE `data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `temperature` varchar(256) NOT NULL,
    `date` timestamp(2) NOT NULL,
  `time` timestamp(2) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci