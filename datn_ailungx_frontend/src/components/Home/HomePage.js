import { useSelector } from "react-redux";
import { useNavigate } from 'react-router-dom';
import "./HomePage.css"
import HomePageUser from "./HomePageUser";
const HomePage = () => {
    const user = useSelector((state) => state.auth.login.currentUser);
    const navigate = useNavigate();
    return (
        <>
        {user? (
            <HomePageUser/>
        ):(
            <main className="main-home">
                <div className="content-home">
                    <h1 className="h1-home">AI-LungX App</h1>
                    <p className="p-home"> Welcome to our website, where we offer advanced medical imaging solutions through deep learning technology. Our expertise lies in accurately diagnosing X-ray images with the help of state-of-the-art algorithms and deep learning. Our mission is to provide an efficient and reliable diagnosis to healthcare professionals, thus enabling them to make informed decisions about patient care. Our cutting-edge technology is designed to revolutionize the field of medical imaging and improve patient outcomes.
                        </p>
                    <div className="btn-div-home">
                        <button className="btn-home" onClick={() => navigate("/login")}>Get Started</button>
                        <button className="btn-home" onClick={() => navigate("/syndromes")}>Syndromes</button>
                    </div>
                    
                </div>
                
                <img className="img-home" img src="https://i.ibb.co/nB5wKgy/logo-home2.png?width=656&height=656" alt="None"/>
                
            </main> 
        )}
        </>
    
     );
}
 
export default HomePage;