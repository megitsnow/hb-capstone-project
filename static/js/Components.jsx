function Homepage(props) {
    return (
        <div id="home-banner" className="row">
        <div className="col">
            <h1>Homepage</h1>
            <p>Homepage</p>
        </div>
        </div>
    );
    }

// Constructors 

function Constructors(props) {
    const constructor_logos  = props
    const logo_components = []
    for (let i = 0; i < constructor_logos.photos.length; i++ ){
        const logo = (
            <ConstructorLogo img = {constructor_logos.photos[i]} 
            key = {constructor_logos.photos[i]}/>
        );
        logo_components.push(logo)
    }
    return (
    <div>
        <h3>Current Constructors</h3>
        <div className = "logo-grid">
            {logo_components}
        </div>
    </div>
    );
}

function ConstructorLogo(props) {
    const img = props
    return (
        <div className = "logos">
           <img src = {img['img']}/> 
        </div>
    );
}

// News

function RecentNews(props) {

}

function Navbar(props) {
    const { logo, brand } = props;

return (
    <nav>
    <section className = "nav-bar">
        <ReactRouterDOM.Link to="/">
            <img src={logo} height="30" alt="logo" />
        </ReactRouterDOM.Link>

        <ReactRouterDOM.NavLink
        to="/drivers">
        <h3>Drivers</h3>
        </ReactRouterDOM.NavLink>

        <ReactRouterDOM.NavLink
        to="/constructors">
        <h3>Constructors</h3>
        </ReactRouterDOM.NavLink>

        <ReactRouterDOM.NavLink
        to="/recent_news">
        <h3>Recent News</h3>
        </ReactRouterDOM.NavLink>
    </section>
    </nav>
    );
}