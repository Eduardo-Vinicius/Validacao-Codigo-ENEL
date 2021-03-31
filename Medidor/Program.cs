using System;

namespace Medidor
{
    class Program
    {
        static string ValidaMedidor(string medida){
            string medidor = medida.Substring(70,10);
            if(!(medidor.IndexOf(" ") >= 0) || medidor == "0000000000")
                medidor = "medida okay";
            else
                medidor = "medida invalida";
            return medidor;
        }
        static void Main(string[] args)
        {
            string linha = "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(ValidaMedidor(linha));
        }
    }
}
