# Bank Transaction Fraud Detection  

## Enlaces  

- [Descripción del dataset](https://www.dynamicduniya.in/dataset/bank-transaction-fraud-detection)  
- [Descargar dataset](https://www.kaggle.com/datasets/marusagar/bank-transaction-fraud-detection)

## Estructura de los Datos (CSV)

| **Índice** | **Variable**                | **Significado**                                                       | **Tipo de Dato**  |
|--------|-------------------------|------------------------------------------------------------------|--------------|
| 1      | Customer_ID             | Identificador del cliente en el sistema de banco.              | String       |
| 2      | Customer_Name           | Nombre del cliente.                                            | String       |
| 3      | Gender                 | Género del cliente.                                            | String       |
| 4      | Age                    | Edad del cliente.                                              | Int          |
| 5      | State                  | Estado donde reside el cliente.                                | String       |
| 6      | City                   | Ciudad donde vive el cliente.                                  | String       |
| 7      | Bank_Branch            | Sucursal bancaria donde el cliente tiene su cuenta.           | String       |
| 8      | Account_Type           | Tipo de cuenta (por ejemplo ahorro) del cliente.              | String       |
| 9      | Transaction_ID         | Identificador para la transacción.                            | String       |
| 10     | Transaction_Date       | Fecha de la transacción.                                      | String       |
| 11     | Transaction_Time       | Hora de la transacción.                                       | String       |
| 12     | Transaction_Amount     | Monto de la transacción.                                      | Float        |
| 13     | Merchant_ID            | Comerciante/establecimiento donde se realiza la transacción.  | String       |
| 14     | Transaction_Type       | Tipo de transacción.                                          | String       |
| 15     | Merchant_Category      | Tipo de negocio del comerciante/establecimiento.             | String       |
| 16     | Account_Balance        | Saldo en la cuenta del cliente después de la transacción.     | Float        |
| 17     | Transaction_Device     | Tipo de plataforma o entorno desde donde se realizó la transacción. | String  |
| 18     | Transaction_Location   | Ubicación geográfica de donde se hizo la transacción.         | String       |
| 19     | Device_Type            | Tipo de dispositivo físico usado en la transacción.           | String       |
| 21     | Transaction_Currency   | Tipo de moneda utilizada en la transacción.                   | String       |
| 22     | Customer_Contact       | Número de teléfono del cliente.                               | String       |
| 23     | Transaction_Description | Descripción breve del tipo de transacción (motivo).         | String       |
| 24     | Customer_Email         | Correo electrónico del cliente.                               | String       |

## Diseño del Modelo de Datos

### Estructura de Nodos

| **Nodo**          | **Atributos (Variables)**                                      | **Tipo de Dato**  |
|--------------|------------------------------------------------------------|--------------|
| **Customer**  | Customer_ID (Identificador del cliente)                   | String       |
|              | Customer_Name (Nombre del cliente)                         | String       |
|              | Gender (Género del cliente)                                | String       |
|              | Age (Edad del cliente)                                     | Int        |
|              | State (Estado donde reside el cliente)                     | String       |
|              | City (Ciudad donde vive el cliente)                        | String       |
|              | Customer_Contact (Número de teléfono del cliente)          | String       |
|              | Customer_Email (Correo electrónico del cliente)            | String       |
| **Bank_Account** | Account_Type (Tipo de cuenta del cliente)             | String       |
|              | Bank_Branch (Sucursal bancaria donde tiene la cuenta)      | String       |
|              | Account_Balance (Saldo en la cuenta después de la transacción) | Float |
| **Transaction** | Transaction_ID (Identificador de la transacción)        | String       |
|              | Transaction_Date (Fecha de la transacción)                 | String       |
|              | Transaction_Time (Hora de la transacción)                  | String       |
|              | Transaction_Amount (Monto de la transacción)               | Float      |
|              | Transaction_Type (Tipo de transacción)                     | String       |
|              | Transaction_Description (Descripción breve del tipo de transacción) | String |
|              | Transaction_Currency (Moneda usada en la transacción)      | String       |
|              | Transaction_Location (Ubicación geográfica de la transacción) | String  |
|              | Is_Fraud (Indicador de si la transacción es fraudulenta)   | Int        |
| **Merchant**  | Merchant_ID (Identificador del comerciante/establecimiento) | String  |
|              | Merchant_Category (Categoría del comerciante/establecimiento) | String |
| **Device**    | Device_Type (Tipo de dispositivo físico usado)            | String       |
|              | Transaction_Device (Plataforma o entorno de la transacción) | String  |

### Relaciones

Customer 


### Diagrama de Modelo de Datos

![Modelación de Datos](./images/modelacion_datos.png "Modelación de Datos")

> **Nota:** Se descartará la columna con el atributo `Is_Fraud` para hacer la exploración sin tener conocimientos del veredicto de la transacción y utilizar las herramientas propuestas para determinar si es o no una transacción fraudulenta.
