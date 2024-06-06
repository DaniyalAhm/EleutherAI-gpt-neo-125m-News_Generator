import React from "react";
import axios from "axios";

const Generate_articles = () => {
    const [articles, setArticles] = React.useState(['Article will appear here']);
    const [loading, setLoading] = React.useState(true);
    const [topic, setTopic] = React.useState("");

    const handleChange = (e) => {
        setTopic(e.target.value);
    }

    const handleSubmit = (e) => {
        e.preventDefault();
        setLoading(true);
        setArticles(['Loading...']);
        axios.get(`http://localhost:5000/MakeNews?topic=${topic}`) // Use backticks for template literals
            .then((response) => {

                setArticles(response.data);
                setLoading(false);
            })
            .catch((error) => {
                console.log(error);
            });
        }


    return (
        <div >
            <h1>Generate Articles</h1>
                <input type="text" placeholder="Enter a topic" onChange={handleChange} />
                <button  onClick={handleSubmit}>Generate Articles</button>

                <h1 className="article-box">{articles}</h1>



        </div>
    )
}
export default Generate_articles;