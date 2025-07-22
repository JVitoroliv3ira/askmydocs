import { Link } from "react-router-dom";
import NotFoundImage from "../assets/404.svg";

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-base-100 text-base-content px-6 py-12 space-y-12">
      <div className="text-lg font-semibold opacity-80 select-none">
        AskMyDocs
      </div>

      <img
        src={NotFoundImage}
        alt="Página não encontrada"
        className="w-72 opacity-80"
      />

      <div className="text-center space-y-2">
        <h1 className="text-5xl font-light opacity-80">404</h1>
        <p className="text-sm opacity-60">Oops! Não encontramos essa página.</p>
      </div>

      <Link
        to="/"
        className="text-sm opacity-70 hover:opacity-100 transition-opacity underline"
      >
        Voltar para a página inicial
      </Link>
    </div>
  );
}
