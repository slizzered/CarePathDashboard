import Styles from "./Layout.module.css";

export function Layout(props) {
  return (
    <>
      <header className={Styles.header}>
        <h1>header</h1>
      </header>

      <main>{props.children}</main>
      <footer className={Styles.footer}>
        <h1>footer</h1>
      </footer>
    </>
  );
}
