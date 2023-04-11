import Link from "next/link";
import Styles from "./Layout.module.css";

export default function Layout(props) {
  return (
    <>
      <header className={Styles.header}>
        <div className={Styles.header_bar}>
          <h1>Carepath-Dashboard</h1>
        </div>
      </header>
      <main className={Styles.main}>{props.children}</main>
      <footer className={Styles.footer}>
        <nav className={Styles.footer_bar}>
          <Link className={Styles.legal_informations} href="">
            AGB
          </Link>
          <Link className={Styles.legal_informations} href="">
            Datenschutzerklärung
          </Link>
          <Link className={Styles.legal_informations} href="">
            Impressum
          </Link>
        </nav>
      </footer>
    </>
  );
}
