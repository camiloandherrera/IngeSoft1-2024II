import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
//import Login from "../pages/Login";
//import Dashboard from "../pages/Dashboard";
import Proyectos from "../pages/Proyectos";

const AppRoutes = () => {
  return (
    <Router>
      <Routes>
        <Route path="/proyectos" element={<Proyectos />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
