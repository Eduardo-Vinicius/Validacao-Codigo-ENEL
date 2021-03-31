using System;

namespace aparelho
{
    class Program
    {
        static string VerificaAparelho(string ap){
            string app = ap.Substring(80,2);
            int nAp = Convert.ToInt32(app);
            if(nAp > 14)
                app = "aparelho não exite";
            else
                app = "aparelho okay";
            
            return app;
        }
        static void Main(string[] args)
        {
            string linha =  "00000348340483300100051Bloco 1A apto 44    ##SSP29Março     20211544230007A16894030000840001550";
            Console.WriteLine(VerificaAparelho(linha));
        }
    }
}
