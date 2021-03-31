using System;

namespace hora
{
    class Program
    {
        static string ValidaHora(string H){
            string hour = H.Substring(64,2);
            int hora = Convert.ToInt32(hour);
            if(hora > 23 || hora == 0)
                hour = "hora não é valida";
            else
                hour = "hora okay";
            return hour;
        }
        static string ValidaMin(string M){
            string min = M.Substring(66,2);
            int minuto = Convert.ToInt32(min);
            if(minuto > 59)
                min = "hora não é valida";
            else
                min = "hora okay";
            return min;
        }
        static string ValidaSeg(string S){
            string seg = S.Substring(68,2);
            int segundo = Convert.ToInt32(seg);
            if(segundo > 59)
                seg = "hora não é valida";
            else
                seg = "hora okay";
            return seg;
        }

        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(ValidaHora(linha));
        }
    }
}
