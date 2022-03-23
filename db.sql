-- MariaDB dump 10.19  Distrib 10.6.5-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: blogging_final
-- ------------------------------------------------------
-- Server version	10.6.5-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `blog_post`
--

DROP TABLE IF EXISTS `blog_post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_post` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `content` text COLLATE utf8mb4_bin NOT NULL,
  `created_at` date NOT NULL DEFAULT current_timestamp(),
  `user_id` int(10) unsigned NOT NULL,
  `header` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `blog_pic` varchar(300) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_post_FK` (`user_id`),
  CONSTRAINT `blog_post_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_post`
--

LOCK TABLES `blog_post` WRITE;
/*!40000 ALTER TABLE `blog_post` DISABLE KEYS */;
INSERT INTO `blog_post` VALUES (1,'Benchmarking involves looking at every element of what you offer and comparing it to the very best element of any of your competitors. So your door handle is as good as the Audi’s, and your brake pedal is as good as the Volvo’s and… It’s pretty tempting to do this. Who wants any element of what they do to be inferior to a competitor’s? And yet… That’s almost never what makes something remarkable (it’s worth noting that the Ford Taurus was the car that brought benchmarking to my attention… who wants a Ford Taurus?). What makes something remarkable is a combination of its internal synergy—the parts work together as a coherent whole—and its imbalance. Something about it is worth talking about. Something about it is hard to find. Something about it helps us achieve our goals if we talk about it. This uneven allocation of attention is the opposite of benchmarking. Find your edge and go over it.','2022-03-10',2,'People loved Toronto\'s full worm moon and shared amazing photos','https://i.postimg.cc/pTsv6GpW/blog-pic.jpg'),(5,'“You can’t be a programmer. You’re too creative.”\n\nChristine Beaubrun, a web developer at Crew, heard this from two different people when she first contemplated a career in tech.\n\nAfter spending a few years in the hospitality industry, Beaubrun didn’t feel satisfied with her career and decided to return to what she knew—art. It’s always been a passion of hers and what she earned her undergraduate degree in. So, she decided to go back to school, this time pursuing a master’s in design and technology. She had every intention of becoming a graphic designer.\n\nAs part of her application to graduate school at Parsons Paris, she created a digital magazine. It was while doing this that she developed a strong interest in tech. To complete the magazine, she used Adobe Creative Suite and also started to dabble in CSS, HTML, and JavaScript. To her surprise, she really loved using those tools.\n\n“It was the first time I’d ever built anything so large and widely accessible on the web, and I was hooked on that feeling,” Beaubrun shares. “It dawned on me—I should really be a front-end engineer because it combines my interests in art, graphic design, and hospitality (which, in this field, is the user experience).”\n\nBut, because she wasn’t fully confident she could pull this new dream off, she decided to “test the waters” and ask family, friends, and some of her colleagues for advice. And that’s where the naysayers—two co-workers who’d only known her for a few months when she was working in the hospitality world—come in.\n\n“Their words inspired me to prove them wrong,” Beaubrun explains. “Plus, I knew the only way I could confirm with certainty whether I was ‘too creative’ or not was to give it a shot.”\n\nSo, Beaubrun left behind her plans to become a graphic designer and never attended Parsons. Instead, she enrolled in the Flatiron School Fellowship Program, where she dove into a five-month-long full-time program focused on helping students start a software engineering career.\n\nDuring her last month of the program, they introduced Beaubrun to a representative at Intel. Intel invited her to participate in their interviewing process, which, in addition to a phone screening call and standard interview, included a technical challenge. She completed all three components remotely since Intel was in California and, at the time, she was based in New York.\n\nOne month later, just half a year after she was told she couldn’t do it—twice—she got an offer to be a front-end engineer at Intel. She stayed there for two years before accepting a role at Crew, where she developed a custom data analytics tool that tracks page activity and writes code to build new features for the Crew app.\n\nBeaubrun loves what she does and finally feels like she’s in the right field.\n\n“I really enjoy talking through problems and figuring out what the best solution may be,” she shares. “When the design team sketches out a solution, I like to jump in and help determine what’s possible or what needs a little more work. From there, I love seeing the final draft of the design, coding it, and presenting it to the team.”\n\nShe loves being in tech so much that she became a member of /dev/color, a nonprofit organization focused on creating “environments where Black software engineers can learn from one another and hold each other accountable for reaching ambitious career goals,” she explains.\n\n/dev/color, she says, has helped her move her career (and life) from the east coast to the west coast when she took the job at Intel, confidently transition from a large company to a startup, and be a better engineer overall.\n\nAll we can say is that it’s quite fortunate she ignored all those pessimists.','2022-03-19',2,'Totally not stolen from a website','https://i.postimg.cc/pTsv6GpW/blog-pic.jpg'),(6,'test','2022-03-22',2,'Test','test');
/*!40000 ALTER TABLE `blog_post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_rating`
--

DROP TABLE IF EXISTS `blog_rating`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_rating` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `blog_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_rating_FK` (`blog_id`),
  KEY `blog_rating_FK_1` (`user_id`),
  CONSTRAINT `blog_rating_FK` FOREIGN KEY (`blog_id`) REFERENCES `blog_post` (`id`),
  CONSTRAINT `blog_rating_FK_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_rating`
--

LOCK TABLES `blog_rating` WRITE;
/*!40000 ALTER TABLE `blog_rating` DISABLE KEYS */;
INSERT INTO `blog_rating` VALUES (5,2,6);
/*!40000 ALTER TABLE `blog_rating` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `content` varchar(750) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `comment_FK` (`user_id`),
  CONSTRAINT `comment_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,1,'test','2022-03-10 20:10:36');
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment_like`
--

DROP TABLE IF EXISTS `comment_like`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment_like` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `comment_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `comment_like_FK` (`comment_id`),
  KEY `comment_like_FK_1` (`user_id`),
  CONSTRAINT `comment_like_FK` FOREIGN KEY (`comment_id`) REFERENCES `comment` (`id`),
  CONSTRAINT `comment_like_FK_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment_like`
--

LOCK TABLES `comment_like` WRITE;
/*!40000 ALTER TABLE `comment_like` DISABLE KEYS */;
INSERT INTO `comment_like` VALUES (2,1,1);
/*!40000 ALTER TABLE `comment_like` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_session`
--

DROP TABLE IF EXISTS `user_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_session` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(10) unsigned NOT NULL,
  `login_token` varchar(128) COLLATE utf8mb4_bin NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_session_FK` (`user_id`),
  CONSTRAINT `user_session_FK` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_session`
--

LOCK TABLES `user_session` WRITE;
/*!40000 ALTER TABLE `user_session` DISABLE KEYS */;
INSERT INTO `user_session` VALUES (13,2,'SLP64Ww-dPG-t6BylsSISR5YWYF60j1sqhg76Dnx39t8seDWPidiOY5Mo4Ta3LqV9gVQh2k4XdzBvO9SjO455MoqzO7KYw'),(14,2,'ESgs39rhps6ehqImjFFhFrp42DO5z0kcGOLaikmJMfrwrWWYuMGHxrIp2_jT99L-OBIdob7IfhGN44kMR-0da5gqwfc2yA'),(15,2,'qd60RB00l9GremzwAYByYcvDyyWP3U3O39yQ2n4B1PKKcTbrOBROAU5LIcW8TsTCLmg-617di8wxgEndbdIzGN8Iy-1mkg'),(16,2,'BThlG_maJiVWQvf4ic26mZh_7IsIg1C_0kSq17NUWzZmyPRtc8Gdm6RzOPdIruTb6w_-q0dglt4TPtFl_E7pIHwCTwKs4A'),(17,2,'VE8_8y7i0C58hp1fax00rQB3ViLmOtL__jwyepq5st1aKcLZyrqFO0HnR25tIm0Hj3xPrr_-eU0dkD-twZGQAEQXZWp13Q'),(18,2,'Bb_Fwe8sdlgGlXqJiRkIzzzdBZnBKzxqQGgbiv6Ip7ucB4AZHlsNLL4ZSihLiGHHS1BSm5JEVJIj-Ex_iWCbTsZSJDb5_A'),(19,2,'i1biXHKvX75zS4XIt67n5xip1u3IgD2MohhQMYYy2KQhZmmE35-AFubXvoDGqltFKPbbDSrIhvnjCF-celOLTa5QeOO5-w'),(20,2,'1IARUjcYQqoPYL7da0NQHNg7deIUdwRnMsOnoOq4fWEeN4iIT8zl0lp-waSSgGOICDlGlFnc89yWuw4whhWxFdoOWUV7Lw'),(21,2,'ZbLmJOKCFNEsu776jJBnkMVsFdY8u63GF9sQrXYqt-sk-boT5tPtHOxbysF2pm3RqSQAhPJHcw965Pr8tjMkyso65qjDpA'),(22,2,'uCK9h9ExeBgWC0CXFTiAVrUvl236Qiba4ypGs7bizilbVrffYtVHLtHm42_vTq3QYUTdC-ZBGbHK_gttlB_agyMv-ojc2w'),(23,2,'OjOBcHtoyaT2FhIJO-R2hFnx3KATZJBq5zDWpoobW5ihF1WQ2PxPzJJQzQBL4Wzxn10o7935xD44U-5bwdtN5qk-aFqXKg'),(24,2,'NSM8VIqo7wdjOvzqUW60BIRYw1GMWRFDPXVsiZQgxyw7GoSx2k8wL1VU17l6gal0ydMzOAkW0bXMw5XPfIA4y0shWUi7Wg'),(25,2,'SkBKpXqtTxCT0eEkEzIqP8yyk28O0K9u6xI7BDJkMJaksaByHuq4eYrLX9MsBR1qHp9YF71ZIWMtEiyXK84siUs-pQ7BTg'),(26,2,'fFIAoBSpm9DgTYGCrH4Se6wU9lhZaPrRXNn_lAgttZEbcqzGivKPNpvBeHEw1o_cIyDOPC4tdHNJtdVZg7CGUU6Fi4d7KQ'),(27,2,'9tyHIxHw0smhnLGiJrUY9uamndXpRkZJr9rLb5UM8sZkFJ-Ni1kI1DT_PkV0S7-MwKDggrvzfaOAGsQujkzJPWBSc3mYnQ'),(28,2,'IvN1dgBjYA5MTtzT9DMjmQiB_l02SdqGCMonEmLqy-OGID2oF3msaQSgW8_DVhhFGK2swanW-FY6rVcpehBm8Drvy_cEUA'),(29,2,'8XMN7P07ye3i9XdzQLZ31roiu9S2dAMAfpgiUdugAoV_oX5grgYr49KAhEvkoSwBTK_ibgCVRkaaF3nbgM0c7mZgLvBrTA'),(30,2,'yJQBMphBq0BvBSpk67gfDMGliucX0QzawiTh3tEnG309xE0AkABiGIts9I3gKFBMkgS2OmHwTEjNeo2emm7pfzv4nr8Y9A'),(31,1,'_khwwgj929Yqq345oMNDrrw6TYANRQjVfzt5tjFzLyVMAUjXCI7hokrhAolgHOxUK30OBFultX2Zw8ovd1fidfIM7HIIJw'),(32,2,'Q9OGakMTqaKaP95xKVMVfQI_cN7aCGPf1MG-yN16WiztUVd4wzatGNvSwIY0twCxkAUt0rNMED0bN24MKk8Llc2XmWeprQ'),(33,2,'kcn41csXuivXQV_eXabx8ZzRFnJ-hexb5GzT-86brRk43v0dNRfhb6l7ZUZ2Z2d4KKYWQBrFrqtEOIopQQ1kT9ochXC40w'),(34,2,'d52X8OvD1yF0yvtraiyx0yXyry5EhDrkH0uuMWTywy_XRBhtsEycsiIt2a47WQLyxU4BURC4djvNm3tdgP4ZcDjpqmXNpg'),(35,2,'vQZ8t1pzfp7EcohPvm2OErEepA_Ho4EN65hlOP05wwtbYjtINde5bftw4tKlozJVOy3icgdsbnFKMot8p6ReYaDw88Otkg'),(36,2,'KUWxJSWDlMWdoSDfq05UdVAlp_kF3dsSTOWrfAsV5OELGFIPgJ90LdY_F8wMejIyma-Un6AHUgG41wTshUsN3c0IRocZdA'),(37,2,'4HnXMMsuOwExV4hvFjDDACp843j86zWw-gzq0Jcidytw_hBczOsHgXYCw-PyqW57RG1QwANQPKYejfescH81mK9hMdw_HA'),(38,2,'Bb5ZoRs_xUT1DAAzo6g1eYOam_Purx4cTFThaJWYKASpB1n3zBMkSUsp2BVkMx2kaXTltfm_LXkvTuxhwA4fDYfCDqpVWg'),(39,2,'R2VNj0-8I1Gb0duFe2cFIAl5Qw1ZX-toBUdSq9UC8H_-qmZL7ZUQesMIXlFihMyUMtR6v1IgE3JAGsfJQhMW_LMBrtHLGw');
/*!40000 ALTER TABLE `user_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `password` varchar(150) COLLATE utf8mb4_bin NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp(),
  `email` varchar(100) COLLATE utf8mb4_bin NOT NULL,
  `dob` date NOT NULL,
  `pfp` varchar(1000) COLLATE utf8mb4_bin DEFAULT 'https://media.istockphoto.com/vectors/male-profile-flat-blue-simple-icon-with-long-shadow-vector-id522855255?k=20&m=522855255&s=612x612&w=0&h=fLLvwEbgOmSzk1_jQ0MgDATEVcVOh_kqEe0rqi7aM5A=',
  `profile_banner` varchar(1000) COLLATE utf8mb4_bin DEFAULT 'https://imgs.search.brave.com/ynFgN7M_rkmfBZRKVsaHeHRLE5l0py3IxOEljQhVwOA/rs:fit:882:337:1/g:ce/aHR0cHM6Ly93d3cu/c21hcnR0LmNvbS9z/aXRlcy9kZWZhdWx0/L2ZpbGVzL3B1Ymxp/Yy90d2l0dGVyX2xv/Z29fYmFubmVyXzEy/LmpwZw',
  `bio` varchar(300) COLLATE utf8mb4_bin DEFAULT 'This user has not set up thier bio yet',
  `salt` varchar(25) COLLATE utf8mb4_bin NOT NULL,
  `is_blogger` tinyint(1) NOT NULL DEFAULT 0,
  `is_admin` tinyint(1) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_un` (`username`),
  UNIQUE KEY `users_uk1` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'test','7185dc7c3ed29e1eff8dcae48b3376d508355530253ab5473cc039cc022d6ce8fa767a1e49314bab9f4bf5da8b770a27aaff5a21f852b342771d11700f33b5a1','2022-03-10 19:58:44','test@gmail.com','2001-01-01','test','test','test','65uvP0Bczj-dNg',1,0),(2,'xAtrizy','e4f033e027ca8d409a92bd8a151ac75fb833b986e837a819bf55b259013d2a6a43759a421279e70b465aa1378c02e332b840f93479c8a7223f24a6b146c41db2','2022-03-12 18:56:36','evankeeping21@gmail.com','2001-07-15','https://imgs.search.brave.com/rjECvbxmSx3dNPmGczze6RSJpix9zkEsXRRSOywviTY/rs:fit:512:512:1/g:ce/aHR0cHM6Ly9pbWcu/d2FsbHBhcGVyc2Fm/YXJpLmNvbS9pbWc3/MjAvODMvNzMvaE9U/cHFSLmpwZw','https://wallpapercave.com/wp/wp5449135.jpg','This is a testing bio to see if everything works','Tc7NKBZFcDJbJQ',1,0);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'blogging_final'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-03-23  0:50:34
