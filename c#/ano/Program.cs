using System;
using System.Linq;

namespace ano
{
    class Program
    {
        static string Validaano(string ano){
            string year = ano.Substring(60,4);
            if(year == "0000" || !year.All(char.IsDigit))
                year = "ano não é valido";
            else
                year = "ano Valido";
            return year;
        }
        static void Main(string[] args)
        {
            string txt = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(Validaano(txt));
        }
    }
}
