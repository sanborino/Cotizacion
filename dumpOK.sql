-- phpMyAdmin SQL Dump
-- version 4.4.11
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 28-08-2015 a las 19:23:50
-- Versión del servidor: 5.5.33
-- Versión de PHP: 5.5.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Base de datos: `cotizacion_py`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `Vencidos`()
    NO SQL
BEGIN
UPDATE cotizacion_cotizacion SET estado="Vencido"
WHERE estado="Pendiente" AND fechaFinal<UTC_DATE();
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add usuarios', 7, 'add_usuarios'),
(20, 'Can change usuarios', 7, 'change_usuarios'),
(21, 'Can delete usuarios', 7, 'delete_usuarios'),
(22, 'Can add cotizacion', 8, 'add_cotizacion'),
(23, 'Can change cotizacion', 8, 'change_cotizacion'),
(24, 'Can delete cotizacion', 8, 'delete_cotizacion'),
(25, 'Can add empresa', 9, 'add_empresa'),
(26, 'Can change empresa', 9, 'change_empresa'),
(27, 'Can delete empresa', 9, 'delete_empresa'),
(28, 'Can add estado', 10, 'add_estado'),
(29, 'Can change estado', 10, 'change_estado'),
(30, 'Can delete estado', 10, 'delete_estado'),
(31, 'Can add ingrediente', 11, 'add_ingrediente'),
(32, 'Can change ingrediente', 11, 'change_ingrediente'),
(33, 'Can delete ingrediente', 11, 'delete_ingrediente'),
(34, 'Can add municipio', 12, 'add_municipio'),
(35, 'Can change municipio', 12, 'change_municipio'),
(36, 'Can delete municipio', 12, 'delete_municipio'),
(37, 'Can add receta', 13, 'add_receta'),
(38, 'Can change receta', 13, 'change_receta'),
(39, 'Can delete receta', 13, 'delete_receta'),
(40, 'Can add detalle', 14, 'add_detalle'),
(41, 'Can change detalle', 14, 'change_detalle'),
(42, 'Can delete detalle', 14, 'delete_detalle'),
(43, 'Can add evento', 15, 'add_evento'),
(44, 'Can change evento', 15, 'change_evento'),
(45, 'Can delete evento', 15, 'delete_evento'),
(46, 'Can add perfil', 16, 'add_perfil'),
(47, 'Can change perfil', 16, 'change_perfil'),
(48, 'Can delete perfil', 16, 'delete_perfil'),
(49, 'Can add cliente', 17, 'add_cliente'),
(50, 'Can change cliente', 17, 'change_cliente'),
(51, 'Can delete cliente', 17, 'delete_cliente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$20000$BRR2bMN1XHNW$qfX+Bs0FWpYd6uS4hhrnDY9He4wFHsjbvqKszCEc0gU=', '2015-08-29 00:58:18', 1, 'ricardo', '', '', '', 1, 1, '2015-08-29 00:57:22');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente_cliente`
--

CREATE TABLE `cliente_cliente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `alta` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `evento_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizacion_cotizacion`
--

CREATE TABLE `cotizacion_cotizacion` (
  `id` int(11) NOT NULL,
  `fechaInicial` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `fechaFinal` date NOT NULL,
  `estado` varchar(20) NOT NULL,
  `personas` int(11) DEFAULT NULL,
  `venta` decimal(10,2) DEFAULT NULL,
  `extra` decimal(10,2) DEFAULT NULL,
  `descripcion` varchar(200) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `cliente_id` int(11) NOT NULL,
  `empresa_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cotizacion_cotizacion_receta`
--

CREATE TABLE `cotizacion_cotizacion_receta` (
  `id` int(11) NOT NULL,
  `cotizacion_id` int(11) NOT NULL,
  `receta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(17, 'cliente', 'cliente'),
(5, 'contenttypes', 'contenttype'),
(8, 'cotizacion', 'cotizacion'),
(9, 'empresa', 'empresa'),
(10, 'estado', 'estado'),
(11, 'ingrediente', 'ingrediente'),
(7, 'inicio', 'usuarios'),
(12, 'municipio', 'municipio'),
(14, 'receta', 'detalle'),
(13, 'receta', 'receta'),
(6, 'sessions', 'session'),
(15, 'tipoEvento', 'evento'),
(16, 'usuarios', 'perfil');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2015-08-29 00:57:05'),
(2, 'auth', '0001_initial', '2015-08-29 00:57:07'),
(3, 'admin', '0001_initial', '2015-08-29 00:57:08'),
(4, 'contenttypes', '0002_remove_content_type_name', '2015-08-29 00:57:09'),
(5, 'auth', '0002_alter_permission_name_max_length', '2015-08-29 00:57:09'),
(6, 'auth', '0003_alter_user_email_max_length', '2015-08-29 00:57:09'),
(7, 'auth', '0004_alter_user_username_opts', '2015-08-29 00:57:09'),
(8, 'auth', '0005_alter_user_last_login_null', '2015-08-29 00:57:10'),
(9, 'auth', '0006_require_contenttypes_0002', '2015-08-29 00:57:10'),
(10, 'sessions', '0001_initial', '2015-08-29 00:57:10'),
(11, 'tipoEvento', '0001_initial', '2015-08-29 00:57:52'),
(12, 'cliente', '0001_initial', '2015-08-29 00:57:52'),
(13, 'ingrediente', '0001_initial', '2015-08-29 00:57:53'),
(14, 'receta', '0001_initial', '2015-08-29 00:57:55'),
(15, 'estado', '0001_initial', '2015-08-29 00:57:55'),
(16, 'municipio', '0001_initial', '2015-08-29 00:57:56'),
(17, 'empresa', '0001_initial', '2015-08-29 00:57:56'),
(18, 'cotizacion', '0001_initial', '2015-08-29 00:57:58'),
(19, 'inicio', '0001_initial', '2015-08-29 00:57:58'),
(20, 'usuarios', '0001_initial', '2015-08-29 00:57:58');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('tynvbq67k3xi8greukpei5fnc460r4a0', 'MDY1ZDEwOTk3ZjBhMTdmMmIzZGNiNzZjOGZiZDgzYzIxOTVhMzUyNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjNlZmFiZDkzMTVjOTkwOWU5MzRkNTU5ZjA3MWVkMDMzOTBhZDFjYjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2015-09-12 00:58:18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empresa_empresa`
--

CREATE TABLE `empresa_empresa` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `direccion` varchar(200) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `celular` varchar(10) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `contacto` varchar(50) NOT NULL,
  `municipio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado_estado`
--

CREATE TABLE `estado_estado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ingrediente_ingrediente`
--

CREATE TABLE `ingrediente_ingrediente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `medida` varchar(50) NOT NULL,
  `cantidad` decimal(6,2) NOT NULL,
  `costo` decimal(6,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inicio_usuarios`
--

CREATE TABLE `inicio_usuarios` (
  `id` int(11) NOT NULL,
  `numeroUnico` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `municipio_municipio`
--

CREATE TABLE `municipio_municipio` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `estado_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `receta_detalle`
--

CREATE TABLE `receta_detalle` (
  `id` int(11) NOT NULL,
  `cantidad` decimal(10,2) NOT NULL,
  `valor` decimal(10,2) NOT NULL,
  `estado` tinyint(1) NOT NULL,
  `item_id` int(11) NOT NULL,
  `receta_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `receta_receta`
--

CREATE TABLE `receta_receta` (
  `id` int(11) NOT NULL,
  `nombre` varchar(250) NOT NULL,
  `creado` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `estado` tinyint(1) NOT NULL,
  `costo` decimal(10,2) DEFAULT NULL,
  `venta` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Disparadores `receta_receta`
--
DELIMITER $$
CREATE TRIGGER `modificaEstado` AFTER UPDATE ON `receta_receta`
 FOR EACH ROW UPDATE receta_detalle
SET estado=0
WHERE estado=1
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoEvento_evento`
--

CREATE TABLE `tipoEvento_evento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios_perfil`
--

CREATE TABLE `usuarios_perfil` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  ADD KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `content_type_id` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  ADD KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`);

--
-- Indices de la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cliente_clien_evento_id_40678d734afca98d_fk_tipoEvento_evento_id` (`evento_id`);

--
-- Indices de la tabla `cotizacion_cotizacion`
--
ALTER TABLE `cotizacion_cotizacion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cotizacion_cot_cliente_id_39acb780b3e185c9_fk_cliente_cliente_id` (`cliente_id`),
  ADD KEY `cotizacion_cot_empresa_id_3d88b5edc081ba80_fk_empresa_empresa_id` (`empresa_id`);

--
-- Indices de la tabla `cotizacion_cotizacion_receta`
--
ALTER TABLE `cotizacion_cotizacion_receta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cotizacion_id` (`cotizacion_id`,`receta_id`),
  ADD KEY `cotizacion_cotiza_receta_id_5c7e0315c4abe6d4_fk_receta_receta_id` (`receta_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_de54fa62` (`expire_date`);

--
-- Indices de la tabla `empresa_empresa`
--
ALTER TABLE `empresa_empresa`
  ADD PRIMARY KEY (`id`),
  ADD KEY `empresa__municipio_id_2d568d52ee3df76a_fk_municipio_municipio_id` (`municipio_id`);

--
-- Indices de la tabla `estado_estado`
--
ALTER TABLE `estado_estado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ingrediente_ingrediente`
--
ALTER TABLE `ingrediente_ingrediente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inicio_usuarios`
--
ALTER TABLE `inicio_usuarios`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `usuario_id` (`usuario_id`);

--
-- Indices de la tabla `municipio_municipio`
--
ALTER TABLE `municipio_municipio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `municipio_municip_estado_id_1662a841fbce455c_fk_estado_estado_id` (`estado_id`);

--
-- Indices de la tabla `receta_detalle`
--
ALTER TABLE `receta_detalle`
  ADD PRIMARY KEY (`id`),
  ADD KEY `receta_det_item_id_955cb39b0998325_fk_ingrediente_ingrediente_id` (`item_id`),
  ADD KEY `receta_detalle_b81fb5e8` (`receta_id`);

--
-- Indices de la tabla `receta_receta`
--
ALTER TABLE `receta_receta`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipoEvento_evento`
--
ALTER TABLE `tipoEvento_evento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios_perfil`
--
ALTER TABLE `usuarios_perfil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=52;
--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `cotizacion_cotizacion`
--
ALTER TABLE `cotizacion_cotizacion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `cotizacion_cotizacion_receta`
--
ALTER TABLE `cotizacion_cotizacion_receta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT de la tabla `empresa_empresa`
--
ALTER TABLE `empresa_empresa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `estado_estado`
--
ALTER TABLE `estado_estado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `ingrediente_ingrediente`
--
ALTER TABLE `ingrediente_ingrediente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `inicio_usuarios`
--
ALTER TABLE `inicio_usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `municipio_municipio`
--
ALTER TABLE `municipio_municipio`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `receta_detalle`
--
ALTER TABLE `receta_detalle`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `receta_receta`
--
ALTER TABLE `receta_receta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `tipoEvento_evento`
--
ALTER TABLE `tipoEvento_evento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `usuarios_perfil`
--
ALTER TABLE `usuarios_perfil`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `cliente_cliente`
--
ALTER TABLE `cliente_cliente`
  ADD CONSTRAINT `cliente_clien_evento_id_40678d734afca98d_fk_tipoEvento_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `tipoEvento_evento` (`id`);

--
-- Filtros para la tabla `cotizacion_cotizacion`
--
ALTER TABLE `cotizacion_cotizacion`
  ADD CONSTRAINT `cotizacion_cot_cliente_id_39acb780b3e185c9_fk_cliente_cliente_id` FOREIGN KEY (`cliente_id`) REFERENCES `cliente_cliente` (`id`),
  ADD CONSTRAINT `cotizacion_cot_empresa_id_3d88b5edc081ba80_fk_empresa_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `empresa_empresa` (`id`);

--
-- Filtros para la tabla `cotizacion_cotizacion_receta`
--
ALTER TABLE `cotizacion_cotizacion_receta`
  ADD CONSTRAINT `cotizacion_cotiza_receta_id_5c7e0315c4abe6d4_fk_receta_receta_id` FOREIGN KEY (`receta_id`) REFERENCES `receta_receta` (`id`),
  ADD CONSTRAINT `cotiz_cotizacion_id_39b73b1b3fdb4e45_fk_cotizacion_cotizacion_id` FOREIGN KEY (`cotizacion_id`) REFERENCES `cotizacion_cotizacion` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `empresa_empresa`
--
ALTER TABLE `empresa_empresa`
  ADD CONSTRAINT `empresa__municipio_id_2d568d52ee3df76a_fk_municipio_municipio_id` FOREIGN KEY (`municipio_id`) REFERENCES `municipio_municipio` (`id`);

--
-- Filtros para la tabla `inicio_usuarios`
--
ALTER TABLE `inicio_usuarios`
  ADD CONSTRAINT `inicio_usuarios_usuario_id_332fa7a75e6ca035_fk_auth_user_id` FOREIGN KEY (`usuario_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `municipio_municipio`
--
ALTER TABLE `municipio_municipio`
  ADD CONSTRAINT `municipio_municip_estado_id_1662a841fbce455c_fk_estado_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `estado_estado` (`id`);

--
-- Filtros para la tabla `receta_detalle`
--
ALTER TABLE `receta_detalle`
  ADD CONSTRAINT `receta_detalle_receta_id_300408bd16cfc9a6_fk_receta_receta_id` FOREIGN KEY (`receta_id`) REFERENCES `receta_receta` (`id`),
  ADD CONSTRAINT `receta_det_item_id_955cb39b0998325_fk_ingrediente_ingrediente_id` FOREIGN KEY (`item_id`) REFERENCES `ingrediente_ingrediente` (`id`);

--
-- Filtros para la tabla `usuarios_perfil`
--
ALTER TABLE `usuarios_perfil`
  ADD CONSTRAINT `usuarios_perfil_user_id_fbdc241e5ca5c90_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

DELIMITER $$
--
-- Eventos
--
CREATE DEFINER=`root`@`localhost` EVENT `revisarVencidos` ON SCHEDULE EVERY 1 DAY STARTS '2015-08-18 00:00:00' ON COMPLETION NOT PRESERVE ENABLE DO CALL Vencidos()$$

DELIMITER ;
