module Meteorologia {
    struct MedicionDia{
        string dia;
        string text;
        string tempMin;
        string tempMax;
        string humedad;
        string viento;
        string vientoDireccion;
    }
    struct MedicionHora{
        string dia;
        string hora;
        string temp;
        string text;
        string humedad;
        string viento;
        string vientoDireccion;
    }

    sequence <MedicionDia> Mediciones;
    sequence <MedicionHora> MedicionesHora;
    interface Conexion
    {
        Mediciones reporteSemanal(string ciudad);
	MedicionesHora reportePorHora(string ciudad);

    }


}
