import { useRouter } from 'next/router'
import { DashBoardHeader } from '../../components/DashboardHeader'
import styles from '../../styles/vaga.module.scss'

export default function Vaga() {
	const router = useRouter()
	return (
		<>
			<DashBoardHeader />
			<div className={styles.container}>
				<div className={styles.content}>
					<div>Essa é a vaga de número {router.query.id}</div>
				</div>
			</div>
		</>
	)
}
