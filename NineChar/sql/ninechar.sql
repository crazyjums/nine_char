/*
Navicat MySQL Data Transfer

Source Server         : craw
Source Server Version : 50724
Source Host           : localhost:3306
Source Database       : ninechar

Target Server Type    : MYSQL
Target Server Version : 50724
File Encoding         : 65001

Date: 2019-04-29 20:34:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `test_result`
-- ----------------------------
DROP TABLE IF EXISTS `test_result`;
CREATE TABLE `test_result` (
  `test_id` int(40) NOT NULL AUTO_INCREMENT,
  `user_id` int(40) DEFAULT NULL,
  `username` char(40) DEFAULT NULL,
  `NO_1` int(10) DEFAULT '0',
  `NO_2` int(10) DEFAULT '0',
  `NO_3` int(10) DEFAULT '0',
  `NO_4` int(10) DEFAULT '0',
  `NO_5` int(10) DEFAULT '0',
  `NO_6` int(10) DEFAULT '0',
  `NO_7` int(10) DEFAULT '0',
  `NO_8` int(10) DEFAULT '0',
  `NO_9` int(10) DEFAULT '0',
  `test_time` datetime DEFAULT NULL,
  `test_type` char(20) DEFAULT NULL,
  PRIMARY KEY (`test_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of test_result
-- ----------------------------
INSERT INTO `test_result` VALUES ('1', '1', 'admin', '14', '12', '12', '12', '13', '11', '10', '11', '11', '2019-04-23 23:27:26', '108');
INSERT INTO `test_result` VALUES ('8', '1', 'admin', '14', '12', '12', '12', '13', '11', '10', '11', '12', '2019-04-23 19:24:02', '108');
INSERT INTO `test_result` VALUES ('9', '2', 'jums', '14', '12', '12', '12', '13', '11', '10', '11', '12', '2019-04-23 19:24:58', '108');
INSERT INTO `test_result` VALUES ('10', '1', 'admin', '23', '9', '14', '15', '8', '13', '24', '16', '22', '2019-04-24 22:46:43', '144');
INSERT INTO `test_result` VALUES ('11', '2', 'jums', '6', '5', '7', '8', '10', '7', '7', '8', '11', '2019-04-29 13:19:26', '108');
INSERT INTO `test_result` VALUES ('12', '2', 'jums', '15', '19', '12', '20', '15', '22', '8', '14', '19', '2019-04-29 14:26:44', '144');

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `user_id` int(20) NOT NULL AUTO_INCREMENT,
  `username` char(40) DEFAULT NULL,
  `password` char(40) DEFAULT NULL,
  `nickname` char(40) DEFAULT NULL,
  `tel` char(11) DEFAULT NULL,
  `back` text,
  `times` int(10) DEFAULT '0',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', 'admin', 'admin', '管理员', '101', '无', '3');
INSERT INTO `user` VALUES ('2', 'jums', 'jums', '汤姆斯', '221', '没有', '3');
