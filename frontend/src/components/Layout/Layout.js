import Styles from "./Layout.module.css";

export default function Layout(props) {
  return (
    <>
      <header className={Styles.header}>header</header>
      <main>{props.children}</main>
      <footer className={Styles.footer}>footer</footer>
    </>
  );
}
