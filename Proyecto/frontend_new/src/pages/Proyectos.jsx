import { proyectos } from "../data/proyectos";

const Proyectos = () => {
  return (
    <div className="p-5">
      <h2 className="text-xl font-bold">Lista de Proyectos</h2>
      <ul className="mt-3">
        {proyectos.map((proyecto) => (
          <li key={proyecto.id} className="border p-3 mb-2 rounded-lg shadow">
            <h3 className="font-semibold">{proyecto.titulo}</h3>
            <p>{proyecto.descripcion}</p>
            <span className="text-sm text-gray-600">Estado: {proyecto.estado}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Proyectos;
