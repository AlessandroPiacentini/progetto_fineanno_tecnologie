-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mag 29, 2024 alle 12:19
-- Versione del server: 10.4.32-MariaDB
-- Versione PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `gestione_spese`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `spese`
--

CREATE TABLE `spese` (
  `id` int(11) NOT NULL,
  `id_user` int(11) DEFAULT NULL,
  `titolo` text NOT NULL,
  `dettagli` text DEFAULT NULL,
  `prezzo` double DEFAULT NULL,
  `data` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `spese`
--

INSERT INTO `spese` (`id`, `id_user`, `titolo`, `dettagli`, `prezzo`, `data`) VALUES
(12, 1, 'titolo12', 'dettagli12', 120, '2024-01-12'),
(13, 1, 'titolo13', 'dettagli13', 130, '2024-01-13'),
(14, 1, 'titolo14', 'dettagli14', 140, '2024-01-14'),
(15, 1, 'titolo15', 'dettagli15', 500, '2024-01-15'),
(16, 1, 'titolo16', 'dettagli16', 160, '2024-05-16'),
(17, 1, 'titolo17', 'dettagli17', 170, '2024-05-17'),
(18, 1, 'titolo18', 'dettagli18', 180, '2024-01-18'),
(19, 1, 'titolo19', 'dettagli19', 190, '2024-01-19'),
(20, 1, 'titolo20', 'dettagli20', 200, '2024-01-20'),
(23, 1, 'prova spesa di oggi', 'lanncnacnacacnac', 20, '2024-05-29'),
(24, 1, 'prova spesa ieri', 'AXABOANXAIOCAJCKJABCABC', 800, '2024-05-28'),
(25, 1, 'spesa del 1900', 'lnxpaonacancancao ni ', 500, '1997-06-04'),
(26, 1, 'prodotto con decimale', 'papxjoajjacaojcpa', 10.5, '2024-05-04');

-- --------------------------------------------------------

--
-- Struttura della tabella `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `users`
--

INSERT INTO `users` (`id`, `username`, `password`) VALUES
(1, 'Piace', '189bbbb00c5f1fb7fba9ad9285f193d1');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `spese`
--
ALTER TABLE `spese`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`);

--
-- Indici per le tabelle `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `spese`
--
ALTER TABLE `spese`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT per la tabella `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `spese`
--
ALTER TABLE `spese`
  ADD CONSTRAINT `spese_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
