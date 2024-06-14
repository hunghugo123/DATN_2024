
import "./AboutPage.css";
const AboutPage = () => {
    return ( 
        <div className="about-container">
            
            <div className="about-container-intro">
                <div className="about-label-intro">Mission & Vision</div>
                <div className="about-text-intro">Medical diagnosis is a complex and critical task that requires a high level of expertise and experience. However, with advances in deep learning, it is possible to develop computer-based systems to assist in medical diagnosis.

                   <br></br>Our website leverages the power of deep learning algorithms to analyze X-ray images and provide accurate and efficient diagnoses. By uploading your X-ray images, our system can quickly identify potential lung-related abnormalities or health problems with high confidence.

                    Our platform is designed to provide users with a seamless and convenient experience, and our team of medical professionals ensures that diagnoses are extremely reliable.

                    <br></br>"Revolutionize medical imaging with the power of deep learning. Let our technology provide accurate and efficient diagnoses through advanced analysis of X-ray images."
                    <br></br>
                    <br></br>This is the graduation project of the Biomedical Engineering program at Ho Chi Minh City University of Technology and Education (HCMUTE). 
                    The product was conceptualized and designed by two members, Hoang Dinh Thuc and Le Thi Anh Thu, with the support of Dr. Nguyen Manh Hung.
                    <br></br>
                    <br></br>Join us as we revolutionize the healthcare industry with the power of deep learning.
                </div>
                {/* <img className="about-img-logo" src="https://i.ibb.co/8bHkZHJ/panel-datn1.png" alt="About logo"></img> */}
                <div className="about-text-intro">
                </div>
            </div>

            <div className="about-container-member">
                <div className="about-label-intro">Our Team</div>
                <div className="about-container-member-info">
                    <img className="about-img-member" src="https://i.ibb.co/xLfR5rC/unnamed.jpg" alt="Member 1"></img>
                    <div className="about-text-member-container">
                        <div className='about-text-member-label'>Name: </div>
                        <div className='about-text-member-result'>Luong Sy Hung</div>
                        <div className='about-text-member-label'>Major & University: </div>
                        <div className='about-text-member-result'>Biomedical Engineering Class of 2020 <br></br> Ho Chi Minh City University Of Technology And Education (HCMUTE)</div>
                    </div>
                </div>
                <div className="about-container-member-info">
                    <img className="about-img-member" src="https://i.ibb.co/qdQjm0n/z5483855243335-d070d387ceb552b11f651ae0e515f02d.jpg" alt="Member 2"></img>
                    <div className="about-text-member-container">
                        <div className='about-text-member-label'>Name: </div>
                        <div className='about-text-member-result'>Huynh Trong Nhan</div>
                        <div className='about-text-member-label'>Major & University: </div>
                        <div className='about-text-member-result'>Biomedical Engineering Class of 2019 <br></br> Ho Chi Minh City University Of Technology And Education (HCMUTE)</div>
                    </div>
                </div>
            </div>
            
            
            
            
            
        </div>
        
    );
}
 
export default AboutPage;