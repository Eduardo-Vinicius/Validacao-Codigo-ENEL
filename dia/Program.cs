using System;

namespace dia
{
    class Program
    {
        static string ValidaDia(string dia){
            string day = dia.Substring(48,2);
            int ndia = Convert.ToInt32(day);
            if(ndia == 0 || ndia > 31)
                day = "Dia não é Valido";
            else
                day = "Dia okay";

            
            return day;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(ValidaDia(linha));
        }
    }
}
