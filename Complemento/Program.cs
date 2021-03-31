using System;
using System.Linq;

namespace Complemento
{
    class Program
    {
        static string VerificaComplemento(string comp){
            string cp = comp.Substring(23,20);
            if(cp.All(char.IsDigit))
                cp = "Complemento é invalido";
            else
                cp = "Complemento está okay";
            return cp;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(VerificaComplemento(linha));
        }
    }
}
