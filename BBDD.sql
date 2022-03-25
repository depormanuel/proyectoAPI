-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 25-03-2022 a las 10:58:22
-- Versión del servidor: 10.4.24-MariaDB
-- Versión de PHP: 8.1.4
USE EventosDeportivos;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Base de datos: `EventosDeportivos`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa`
--

CREATE TABLE `empresa` (
`nombre` varchar(100) NOT NULL,
`ciudad` varchar(100) NOT NULL,
`mail` varchar(100) NOT NULL,
`telefono` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `evento`
--

CREATE TABLE `evento` (
`mes` varchar(20) NOT NULL,
`ano` int(4) NOT NULL,
`instalacion` varchar(100) NOT NULL,
`entidad` varchar(100) NOT NULL,
`actividad` varchar(100) NOT NULL,
`deporte` varchar(100) NOT NULL,
`idEven` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participan`
--

CREATE TABLE `participan` (
`codEven` int(11) NOT NULL,
`codPart` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participante`
--

CREATE TABLE `participante` (
`nombre` varchar(100) NOT NULL,
`idPart` int(11) NOT NULL,
`localidad` varchar(100) NOT NULL,
`telefono` varchar(9) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `empresa`
--
ALTER TABLE `empresa`
ADD PRIMARY KEY (`nombre`);

--
-- Indices de la tabla `evento`
--
ALTER TABLE `evento`
ADD PRIMARY KEY (`idEven`),
ADD KEY `entidad` (`entidad`);

--
-- Indices de la tabla `participan`
--
ALTER TABLE `participan`
ADD KEY `partiEven` (`codEven`),
ADD KEY `partiPart` (`codPart`);

--
-- Indices de la tabla `participante`
--
ALTER TABLE `participante`
ADD PRIMARY KEY (`idPart`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `evento`
--
ALTER TABLE `evento`
MODIFY `idEven` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `participante`
--
ALTER TABLE `participante`
MODIFY `idPart` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `evento`
--
ALTER TABLE `evento`
ADD CONSTRAINT `evento_ibfk_1` FOREIGN KEY (`entidad`) REFERENCES `empresa` (`nombre`);

--
-- Filtros para la tabla `participan`
--
ALTER TABLE `participan`
ADD CONSTRAINT `partiEven` FOREIGN KEY (`codEven`) REFERENCES `evento` (`idEven`),
ADD CONSTRAINT `partiPart` FOREIGN KEY (`codPart`) REFERENCES `participante` (`idPart`);
COMMIT;