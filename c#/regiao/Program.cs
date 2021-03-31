using System;

namespace regiao
{
    class Program
    {
        static string Validaregiao(string texto)
        {
            string reg = texto.Substring(43,5);
            if(reg.Substring(0,2) == "##" && reg.Substring(2,3) == "SSP")
                reg = "Regiao Okay";
            else
                reg = "Regiao Errada";
            return reg;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(Validaregiao(linha));
        }
    }
}
