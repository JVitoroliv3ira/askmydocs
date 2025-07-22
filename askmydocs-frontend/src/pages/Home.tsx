import Layout from "../components/Layout/Layout";
import UploadArea from "../components/UploadArea/UploadArea";
import { useDocumentTitle } from "../hooks/useDocumentTitle";

export default function Home() {
  useDocumentTitle("AskMyDocs");

  return (
    <Layout>
      <div className="flex flex-col items-center text-center space-y-8 max-w-4xl w-full">
        <div className="space-y-2">
          <h1 className="text-lg font-semibold opacity-80">Bem-vindo ao AskMyDocs</h1>
          <p className="text-sm opacity-60">
            Para começar, faça o upload dos documentos que você deseja consultar. 
            Após o envio, o sistema processará os arquivos automaticamente.
          </p>
        </div>

        <UploadArea onFilesSelected={(f) => { console.log(f) }} />
      </div>
    </Layout>
  );
}
