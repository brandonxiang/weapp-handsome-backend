-- phpMyAdmin SQL Dump
-- version 3.3.8.1
-- http://www.phpmyadmin.net
--
-- 主机: w.rdc.sae.sina.com.cn:3307
-- 生成日期: 2017 年 01 月 18 日 11:16
-- 服务器版本: 5.6.23
-- PHP 版本: 5.3.3

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `app_brandonhandsome`
--

-- --------------------------------------------------------

--
-- 表的结构 `validation`
--

CREATE TABLE IF NOT EXISTS `validation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `openid` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=39 ;

--
-- 转存表中的数据 `validation`
--

INSERT INTO `validation` (`id`, `openid`) VALUES
(4, 'martin'),
(28, 'safs'),
(29, 'safs'),
(34, 'martin2'),
(38, 'martin23');

-- --------------------------------------------------------

--
-- 表的结构 `vote`
--

CREATE TABLE IF NOT EXISTS `vote` (
  `name` text NOT NULL,
  `score` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `vote`
--

INSERT INTO `vote` (`name`, `score`) VALUES
('bluebutterfly', 1),
('me', 2);
