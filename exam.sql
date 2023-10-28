-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 24-10-2023 a las 03:33:56
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `exam`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tblexa`
--

CREATE TABLE `tblexa` (
  `Id_Cliente` int(11) NOT NULL,
  `Cuota` int(50) NOT NULL,
  `Monto` decimal(10,2) NOT NULL,
  `Fecha_Pago` date NOT NULL,
  `Fecha_Pago_Realizacion` date DEFAULT NULL,
  `Estado` varchar(50) COLLATE utf8mb4_spanish_ci NOT NULL,
  `Referencia` varchar(120) COLLATE utf8mb4_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

--
-- Volcado de datos para la tabla `tblexa`
--

INSERT INTO `tblexa` (`Id_Cliente`, `Cuota`, `Monto`, `Fecha_Pago`, `Fecha_Pago_Realizacion`, `Estado`, `Referencia`) VALUES
(1, 1, '200.00', '2023-10-01', NULL, 'P', ''),
(1, 2, '200.00', '2023-11-01', NULL, 'P', ''),
(1, 3, '200.00', '2023-12-01', NULL, 'P', ''),
(2, 1, '500.00', '2023-10-01', NULL, 'P', ''),
(2, 2, '500.00', '2023-11-01', NULL, 'P', ''),
(2, 3, '500.00', '2023-12-01', NULL, 'P', ''),
(3, 1, '700.00', '2023-10-01', NULL, 'P', ''),
(3, 2, '700.00', '2023-11-01', NULL, 'P', ''),
(3, 3, '700.00', '2023-12-01', NULL, 'P', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
