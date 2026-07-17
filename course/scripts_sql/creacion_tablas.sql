CREATE TABLE IF NOT EXISTS delivery_zones (
	id_delivery INT AUTO_INCREMENT PRIMARY KEY,
    branch VARCHAR(50),  -- SUCURSAL
    plaza VARCHAR(30), -- PLAZA
    postal_code VARCHAR(10) NOT NULL, -- CODIGO_POSTAL
    township VARCHAR(100) NOT NULL,  -- COLONIA/ASENTAMIENTO
    municipality VARCHAR(150) NOT NULL, -- -- DELEGACIÓN/MUNICIPIO
    city VARCHAR(100) NOT NULL, -- CIUDAD
    state VARCHAR(100) NOT NULL, -- ESTADO
    -- COBERTURA restringida a solo estas 3 opciones
    coverage_type ENUM('PAQUETEXPRESS', 'ZONA PLUS', 'ZONA PLUS ESPECIAL') NOT NULL,
     -- Índice para acelerar las búsquedas por Código Postal
    INDEX idx_postal_code (postal_code)
);

CREATE TABLE IF NOT EXISTS shipments_px (
	id_shiping INT AUTO_INCREMENT PRIMARY KEY,
	name_receiver VARCHAR(100),
    id_folio INT AUTO_INCREMENT,
    rfc VARCHAR(50) NOT NULL, -- SIEMPRE EL MISMO XAXX-010101-000
    country VARCHAR(50) NOT NULL, -- SIEMPRE EL MISMO MEXICO
    city VARCHAR(100) NOT NULL, -- CIUDAD
    state VARCHAR(100) NOT NULL, -- ESTADO
    street VARCHAR(100) NOT NULL, -- CALLE
    num VARCHAR(50) NOT NULL, -- NUIMERO CALLE
    township VARCHAR(100) NOT NULL,  -- COLONIA
    postal_code VARCHAR(10) NOT NULL, -- CODIGO_POSTAL
    email VARCHAR(100), -- EMAIL CONTACTO
    phone VARCHAR(50), -- TELEFONO CONTACTO
    address_reference TEXT NULL,
    quantity INT NOT NULL,
    package_code TINYINT(1) NOT NULL,
    content VARCHAR(100) NOT NULL,
	weight DECIMAL(10, 2) NOT NULL,          -- PESO (ej. 10.50)
    volume DECIMAL(10, 4) NOT NULL,          -- VOLUMEN (se usan más decimales por metros cúbicos)
    length DECIMAL(10, 2) NOT NULL,          -- LARGO
    width DECIMAL(10, 2) NOT NULL,           -- ANCHO
    height DECIMAL(10, 2) NOT NULL
);