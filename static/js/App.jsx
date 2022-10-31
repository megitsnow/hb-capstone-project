function App () {
    const [constructor_logos, setConstructorLogos] = React.useState({});

    React.useEffect(() => {
        fetch('/logo_data')
            .then((response) => response.json())
            .then((result) => {
            setConstructorLogos(result)
            });
        }, []);
    

    return (
    <ReactRouterDOM.BrowserRouter>
    <Navbar logo="https://upload.wikimedia.org/wikipedia/commons/3/33/F1.svg" brand="Ubermelon" />
    <div>
        <ReactRouterDOM.Route exact path="/">
        <Homepage />
        </ReactRouterDOM.Route>

        <ReactRouterDOM.Route exact path="/constructors">
        <Constructors photos = {constructor_logos}/>
        </ReactRouterDOM.Route>
    </div>  
        </ReactRouterDOM.BrowserRouter>
    );
}

ReactDOM.render(<App />, document.querySelector('#root'));


