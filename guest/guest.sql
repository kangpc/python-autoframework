-- phpMyAdmin SQL Dump
-- version 4.8.4
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2019-10-30 12:47:24
-- 服务器版本： 5.7.24
-- PHP 版本： 7.2.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `guest`
--

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add event', 7, 'add_event'),
(26, 'Can change event', 7, 'change_event'),
(27, 'Can delete event', 7, 'delete_event'),
(28, 'Can view event', 7, 'view_event'),
(29, 'Can add guest', 8, 'add_guest'),
(30, 'Can change guest', 8, 'change_guest'),
(31, 'Can delete guest', 8, 'delete_guest'),
(32, 'Can view guest', 8, 'view_guest');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$xAMUvcHjlE40$LitUukskS9o8GJi7YlvURVKSrS0/Wb9PVw8JT33IZ9Y=', '2019-05-08 21:11:48.743804', 1, 'kpc', '', '', 'kpc@mail.com', 1, 1, '2019-04-13 01:25:15.145519');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_unicode_ci,
  `object_repr` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'sign', 'event'),
(8, 'sign', 'guest');

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-04-13 01:20:54.334602'),
(2, 'auth', '0001_initial', '2019-04-13 01:20:54.846631'),
(3, 'admin', '0001_initial', '2019-04-13 01:20:56.527727'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-04-13 01:20:56.900748'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-04-13 01:20:56.912749'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-04-13 01:20:57.103760'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-04-13 01:20:57.185765'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-04-13 01:20:57.286770'),
(9, 'auth', '0004_alter_user_username_opts', '2019-04-13 01:20:57.303771'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-04-13 01:20:57.389776'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-04-13 01:20:57.392776'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-04-13 01:20:57.404777'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-04-13 01:20:57.481782'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-04-13 01:20:57.544785'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-04-13 01:20:57.611789'),
(16, 'auth', '0011_update_proxy_permissions', '2019-04-13 01:20:57.631790'),
(17, 'sessions', '0001_initial', '2019-04-13 01:20:57.695794'),
(18, 'sign', '0001_initial', '2019-04-13 01:20:57.853803'),
(19, 'sign', '0002_guest', '2019-04-13 01:20:57.920807');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf8_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0t9clru0c621bd0cw6tidswsz48gazs3', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-04-27 14:28:35.130034'),
('j054w5ikzuxwm3mjvc0wybog3436ncux', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-04-27 14:48:40.052951'),
('ucor2ucdpltlvz541frnb6fn7eo4pi97', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-04-27 14:49:37.469235'),
('c3jpfph9783i6cm31l0p3j4metwzj2ks', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-04-27 21:25:47.469801'),
('1msw86wclicw9ha4919ta6adcohj7f42', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-05-06 17:07:16.575788'),
('mdy8f0hmzl38w0h7b8qhg8xhc4kleqnc', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-05-05 20:13:25.229980'),
('g9o8mcw5ybafbn8e33p4oap1cjl2d0hi', 'YzcyMWNiMDQ4NDEwODc4N2ZmZjk1NDM2MWFmYjBlMDMyMDQxMmQ2Njp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzOGNkN2EwMjY4OGFlMjMxYjE3MjY1MGJmMGI4OWEzZTk4ZmMxOGYwIiwidXNlciI6ImtwYyJ9', '2019-05-22 21:11:48.782806');

-- --------------------------------------------------------

--
-- 表的结构 `sign_event`
--

DROP TABLE IF EXISTS `sign_event`;
CREATE TABLE IF NOT EXISTS `sign_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
  `limit` int(11) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `address` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `sign_event`
--

INSERT INTO `sign_event` (`id`, `name`, `limit`, `status`, `address`, `start_time`, `create_time`) VALUES
(17, 'nubia X93 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:29:27'),
(1, 'nubia1 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:30:40'),
(2, 'nubia2 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:30:54'),
(3, 'nubia3 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:31:04'),
(4, 'nubia4 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:31:15'),
(5, 'xiaomi5 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:32:01'),
(6, 'xiaomi6 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:32:13'),
(7, '华为7 发布会', 8000, 1, '鸟巢', '2020-01-01 18:00:00.000000', '2019-04-24 16:32:41');

-- --------------------------------------------------------

--
-- 表的结构 `sign_guest`
--

DROP TABLE IF EXISTS `sign_guest`;
CREATE TABLE IF NOT EXISTS `sign_guest` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `realname` varchar(64) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf8_unicode_ci NOT NULL,
  `sign` tinyint(1) NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `event_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sign_guest_event_id_phone_96bd84df_uniq` (`event_id`,`phone`),
  KEY `sign_guest_event_id_fa7638b3` (`event_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 转存表中的数据 `sign_guest`
--

INSERT INTO `sign_guest` (`id`, `realname`, `phone`, `email`, `sign`, `create_time`, `event_id`) VALUES
(1, '张三', '12345001101', 'zhangs@mail.com', 0, '2019-04-13 07:50:52', 2),
(2, '李四', '13900000000', 'lis@mail.com', 0, '2019-04-13 07:50:55', 4),
(3, '康平汆', '13600805241', 'kpc@mail.com', 0, '2019-04-13 07:50:59', 5),
(4, 'andy', '13611001101', 'andy@mail.com', 1, '2019-04-22 16:16:50', 3),
(5, '李五', '13611001102', 'liwu@mail.com', 0, '2019-04-13 11:42:50', 2),
(6, 'lily', '13913301102', 'ww@mail.com', 0, '2019-04-13 13:10:30', 2),
(7, 'vivian', '13913301888', 'vv@mail.com', 1, '2019-04-22 16:18:35', 3),
(8, 'zhangailing', '13913301321', 'zal@mail.com', 0, '2019-04-17 15:41:20', 7),
(9, 'dulala', '13913301322', 'dll@mail.com', 0, '2019-04-17 15:41:28', 3),
(10, 'adu', '13999301322', 'ad@mail.com', 0, '2019-04-18 15:49:52', 7),
(11, 'tester01', '13600800001', 'tester@email.com', 0, '2019-04-21 05:55:07', 1),
(12, 'tester01', '13600800001', 'tester@email.com', 0, '2019-04-21 05:56:09', 3),
(13, 'tester02', '13600800002', 'tester@email.com', 0, '2019-04-22 15:48:44', 3);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
