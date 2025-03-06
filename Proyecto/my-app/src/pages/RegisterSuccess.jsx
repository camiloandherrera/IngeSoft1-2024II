// RegisterSuccess.jsx
import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './RegisterSuccess.css';

const RegisterSuccess = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const timer = setTimeout(() => {
      navigate('/'); // Redirige a la página de inicio de sesión después de unos segundos
    }, 5000); // 5 segundos
    return () => clearTimeout(timer);
  }, [navigate]);

  return (
    <div className="success-container">
      <div className="success-box">
        <img src="/nice.png" alt="Éxito" className="success-icon" />
        <h2>¡Registro exitoso!</h2>
        <p>En breve, será redirigido a la página de inicio de sesión.</p>
        <p>Si no es redirigido automáticamente, <a href="/">click aquí</a>.</p>
      </div>
    </div>
  );
};

export default RegisterSuccess;
