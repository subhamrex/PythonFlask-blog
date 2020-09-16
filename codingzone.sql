-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 16, 2020 at 11:04 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `codingzone`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `SLNo` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phn_no` varchar(50) NOT NULL,
  `msg` text NOT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`SLNo`, `name`, `email`, `phn_no`, `msg`, `date`) VALUES
(1, 'rex', 'rex@gmail.com', '', 'hello brother', '2020-09-13 23:42:01'),
(2, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'uhul', '2020-09-14 03:14:26'),
(3, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'another one', '2020-09-14 03:41:45'),
(4, 'kalirex', 'testpubgmobile007@gmail.com', '89414754', 'yo hackers', '2020-09-14 14:11:56'),
(5, 'kalirex', 'testpubgmobile007@gmail.com', '89414754', 'yo hackers', '2020-09-14 14:21:12'),
(6, 'kalirex', 'testpubgmobile007@gmail.com', '89414754', 'yo hackers', '2020-09-14 14:21:21'),
(7, 'kalirex', 'testpubgmobile007@gmail.com', '89414754', 'yo hackers', '2020-09-14 14:22:42'),
(8, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'dog', '2020-09-14 14:24:10'),
(9, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'dog', '2020-09-14 14:24:55'),
(10, 'kalihackz', 'kali@gmail.com', '0000000', 'I am Kali...best hacker.', '2020-09-14 15:32:11'),
(11, 'kalihackz', 'kali@gmail.com', '0000000', 'I am Kali...best hacker.', '2020-09-14 15:33:52'),
(12, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'me', '2020-09-16 14:18:37'),
(13, 'Subham Kundu', 'subhamkundu486@gmail.com', '+917908428074', 'mefxn', '2020-09-16 14:19:01');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `SLNo` int(11) NOT NULL,
  `title` varchar(50) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `content` text NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `img_file` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`SLNo`, `title`, `slug`, `content`, `date`, `img_file`) VALUES
(1, 'This is my first post title', 'first-post', 'I am so exited.', '2020-09-15 22:24:55', 'post-bg.jpg'),
(2, 'This is my 2nd post title', 'second-post', 'My second post .', '2020-09-14 18:12:59', 'post-bg.jpg'),
(3, 'This is my third post title', 'third-post', 'This is my third post. I  hope you like it.', '2020-09-15 18:33:05', ''),
(4, 'This is my 4th post title', '4th-post', 'I am doing nothing.', '2020-09-16 12:56:20', 'my.jpg'),
(5, 'This is my 5th post title', '5th-post', 'I am writing my 5th post.', '2020-09-16 12:57:32', 'lol.jpg'),
(6, 'This is my 6th post title', '6th-post', 'This is my 6th post.', '2020-09-16 12:59:18', 'big.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`SLNo`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`SLNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `SLNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `SLNo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
