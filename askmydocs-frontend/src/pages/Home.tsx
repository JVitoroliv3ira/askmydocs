import Layout from "../components/Layout/Layout";
import UploadArea from "../components/UploadArea/UploadArea";
import { useDocumentTitle } from "../hooks/useDocumentTitle";

export default function Home() {
  useDocumentTitle("AskMyDocs");

  return (
    <Layout>
      <UploadArea onFilesSelected={(f) => { console.log(f) }} />
    </Layout>
  );
}
