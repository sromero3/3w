SELECT 
    d.id AS documento_id,
    d.numero,
    d.monto,
    SUM(pd.monto_procesar) AS total_abonado,
    MAX(p.fecha) AS fecha_ultimo_pago
FROM app_gestion_documentos d
JOIN app_gestion_pago_detalle pd ON pd.documento_id = d.id
JOIN app_gestion_pagos p ON pd.pago_id = p.id
GROUP BY d.id, d.numero, d.monto
HAVING 
    SUM(pd.monto_procesar) = d.monto AND
    MAX(p.fecha) = '2025-07-04';
