import Layout from "../components/Layout/Layout";
import { useDocumentTitle } from "../hooks/useDocumentTitle";

export default function Home() {
  useDocumentTitle("AskMyDocs");

  return (
    <Layout>
      <h1>Hello, World!</h1>
    </Layout>
  );
}
