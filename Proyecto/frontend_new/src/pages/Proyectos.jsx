// Base version
/*
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
*/

// Tailwind CSS version
import { proyectos } from "../data/proyectos";

const Proyectos = () => {
  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h2 className="text-2xl font-bold text-gray-800 mb-4">Lista de Proyectos</h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {proyectos.map((proyecto) => (
          <li key={proyecto.id} className="bg-white p-4 rounded-lg shadow-md hover:shadow-lg transition-shadow">
            <h3 className="font-semibold text-lg">{proyecto.titulo}</h3>
            <p className="text-gray-600">{proyecto.descripcion}</p>
            <span className={`text-sm font-semibold ${
              proyecto.estado === "En progreso" ? "text-blue-600" : "text-red-600"
            }`}>
              Estado: {proyecto.estado}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Proyectos;


/*
// Material UI version
import { proyectos } from "../data/proyectos";
import { Card, CardContent, Typography } from "@mui/material";

const Proyectos = () => {
  return (
    <div style={{ padding: "20px", backgroundColor: "#f4f4f4", minHeight: "100vh" }}>
      <Typography variant="h4" gutterBottom>
        Lista de Proyectos
      </Typography>
      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(300px, 1fr))", gap: "16px" }}>
        {proyectos.map((proyecto) => (
          <Card key={proyecto.id} style={{ maxWidth: 350, padding: "10px" }}>
            <CardContent>
              <Typography variant="h6">{proyecto.titulo}</Typography>
              <Typography color="textSecondary">{proyecto.descripcion}</Typography>
              <Typography color={proyecto.estado === "En progreso" ? "primary" : "error"}>
                Estado: {proyecto.estado}
              </Typography>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Proyectos;
*/
