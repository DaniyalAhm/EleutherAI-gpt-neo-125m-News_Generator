import logo from './logo.svg';
import './App.css';
import Header from './components/Header';
import Generate_articles from './components/Generate_articles';
import Footer from './components/Foolter';
function App() {
  return (
    <div className="App">
      <Header />
      <Generate_articles  className='Articles'/>
      <Footer />
    </div>

  );
}

export default App;
