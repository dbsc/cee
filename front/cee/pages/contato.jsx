import Head from 'next/head'
import styles from '../styles/contato.module.scss'

export default function Contato() {
	return (
		<>
			<Head>
				<title>Contato | CEE</title>
			</Head>
			<div className={styles.container}>
				<h1>Contato</h1>
			</div>
		</>
	)
}
