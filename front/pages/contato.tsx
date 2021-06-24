import Head from 'next/head'
import { ContatoTitle } from '../components/ContatoTitle'
import { FormsRedes } from '../components/FormsRedes'

export default function Contato() {
	return (
		<>
			<Head>
				<title>Contato | CEE</title>
			</Head>
			<ContatoTitle />
			<FormsRedes />
		</>
	)
}
