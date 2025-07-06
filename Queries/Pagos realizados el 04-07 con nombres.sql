SELECT 
    d.numero,
    c.nombre AS cliente,
    d.monto,
    (SELECT SUM(pd.monto_procesar) 
     FROM app_gestion_pago_detalle pd 
     WHERE pd.documento_id = d.id) AS total_abonado,
    (SELECT MAX(p.fecha) 
     FROM app_gestion_pago_detalle pd
     JOIN app_gestion_pagos p ON pd.pago_id = p.id
     WHERE pd.documento_id = d.id) AS fecha_ultimo_pago
FROM app_gestion_documentos d
JOIN app_gestion_clientes c ON d.cliente_id = c.id
WHERE 
    (SELECT SUM(pd.monto_procesar) 
     FROM app_gestion_pago_detalle pd 
     WHERE pd.documento_id = d.id) = d.monto
AND
    (SELECT MAX(p.fecha) 
     FROM app_gestion_pago_detalle pd
     JOIN app_gestion_pagos p ON pd.pago_id = p.id
     WHERE pd.documento_id = d.id) = '2025-07-04'
ORDER BY c.nombre;



